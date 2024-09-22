import {
    createSIWEConfig,
    formatMessage,
    type SIWECreateMessageArgs,
    type SIWESession,
    type SIWEVerifyMessageArgs,
} from '@reown/appkit-siwe';
import axios from 'axios';
import { SiweMessage } from 'siwe';

const getNonce = async (): Promise<string> => {
    try {
        const {data} = await axios.get('/api/v1/auth/web3/siwe/nonce/');
        console.log(data);
        return data.nonce;
    } catch (error) {
        console.error(error);
    }
}

const verifyMessage = async ({message, signature}: SIWEVerifyMessageArgs) => {
    try {
        const {data} = await axios.post('/api/v1/auth/web3/siwe/verify/', {
            message: message,
            signature: signature,
        });
        console.log(data);
        return data.verify === true;
    } catch (error) {
        return false;
    }
}

const getSession = async () => {
    try {
        const {data} = await axios.get('/api/v1/auth/web3/siwe/session/');
        console.log(data);
        return data == {} ? null : {address: data.address, chainId: data.chain_id} as SIWESession;
    } catch (error) {
        console.error(error);
    }
}

const signOut = async (): Promise<boolean> => {
    try {
        const {data} = await axios.get('/api/v1/auth/web3/siwe/signout/');
        console.log(data);
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
        getMessageParams: async () => ({
            domain: window.location.host,
            uri: window.location.origin,
            chains,
            statement: 'Please sign with your account',
        }),
        createMessage: ({address, ...args}: SIWECreateMessageArgs) => {
            return formatMessage(args, address)
        },
        getNonce,
        getSession,
        verifyMessage,
        signOut,
    });
}
