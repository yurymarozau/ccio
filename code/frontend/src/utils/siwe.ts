import {
    createSIWEConfig,
    formatMessage,
    type SIWECreateMessageArgs,
    type SIWEMessageArgs,
    type SIWESession,
    type SIWEVerifyMessageArgs,
} from '@reown/appkit-siwe';
import axios from 'axios-config';
import { SiweMessage } from 'siwe';

const getMessageParams = async (chains: [number]): Promise<SIWEMessageArgs> => {
    const issued_at = new Date();
    const expiration_date = new Date(issued_at);
    expiration_date.setSeconds(expiration_date.getSeconds() + 3600 * 24 * 30);  // 30 days
    return {
        domain: window.location.host,
        uri: window.location.origin,
        chains,
        exp: expiration_date.toISOString(),
        iat: issued_at.toISOString(),
        statement: 'Please sign with your account',
    }
}

const getNonce = async (): Promise<string> => {
    try {
        const {data} = await axios.get('/api/v1/auth/web3/siwe/nonce/');
        return data.nonce;
    } catch (error) {
        return null;
    }
}

const verifyMessage = async ({message, signature}: SIWEVerifyMessageArgs): Promise<boolean> => {
    try {
        const {data} = await axios.post('/api/v1/auth/web3/siwe/verify/', {
            message: message,
            signature: signature,
        });
        return data.is_verified === true;
    } catch (error) {
        return false;
    }
}

export const getSession = async (): Promise<SIWESession> => {
    try {
        const {data} = await axios.get('/api/v1/auth/web3/siwe/session/');
        return data == {} ? null : {address: data.address, chainId: data.chain_id} as SIWESession;
    } catch (error) {
        return null;
    }
}

const signOut = async (): Promise<boolean> => {
    try {
        const {data} = await axios.get('/api/v1/auth/web3/siwe/signout/');
        return data == {};
    } catch (error) {
        return false;
    }
}

export const createSIWE = (chains: [number]) => {
    return createSIWEConfig({
        enabled: true,
        signOutOnDisconnect: true,
        signOutOnAccountChange: true,
        signOutOnNetworkChange: false,
        getMessageParams: async () => (getMessageParams(chains)),
        createMessage: ({address, ...args}: SIWECreateMessageArgs) => {
            return formatMessage(args, address)
        },
        getNonce: getNonce,
        getSession: getSession,
        verifyMessage: verifyMessage,
        signOut: signOut,
    });
}
