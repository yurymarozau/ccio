import {
    createSIWEConfig,
    formatMessage,
    type SIWECreateMessageArgs,
    type SIWEMessageArgs,
    type SIWESession,
    type SIWEVerifyMessageArgs,
} from '@reown/appkit-siwe';
import axios from 'axios';
import { SiweMessage } from 'siwe';

const getMessageParams = async (chains: [number]): Promise<SIWEMessageArgs> => {
    const issued_at = new Date();
    const expiration_date = new Date(issued_at);
    expiration_date.setSeconds(expiration_date.getSeconds() + 10);
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
        console.error(error);
    }
}

const verifyMessage = async ({message, signature}: SIWEVerifyMessageArgs): Promise<boolean> => {
    try {
        const {data} = await axios.post('/api/v1/auth/web3/siwe/verify/', {
            message: message,
            signature: signature,
        });
        return data.verify === true;
    } catch (error) {
        return false;
    }
}

const getSession = async (): Promise<SIWESession> => {
    try {
        const {data} = await axios.get('/api/v1/auth/web3/siwe/session/');
        return data == {} ? null : {address: data.address, chainId: data.chain_id} as SIWESession;
    } catch (error) {
        console.error(error);
    }
}

const signOut = async (): Promise<boolean> => {
    try {
        const {data} = await axios.get('/api/v1/auth/web3/siwe/signout/');
        return data == {};
    } catch (error) {
        console.error(error);
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
        getNonce,
        getSession,
        verifyMessage,
        signOut,
    });
}
