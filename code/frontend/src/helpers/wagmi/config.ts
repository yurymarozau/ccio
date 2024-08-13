import { http, createConfig } from 'wagmi';
import { sepolia, arbitrumSepolia, lineaSepolia } from 'viem/chains';
import { walletConnect, injected } from 'wagmi/connectors';
import type { CreateConnectorFn } from '@wagmi/core'

// const projectId = import.meta.env.WALLETCONNECT_PROJECT_ID;
const projectId = '9181c8409e9b15913713c456b74335a7'
if (!projectId) throw new Error('Project ID is undefined');

const metadata = {
    name: 'CCIO',
    description: 'CCIO - Crypto Chart IO',
    url: 'ccio',
    icons: ['https://avatars.githubusercontent.com/u/37784886'],
};

const connectors: CreateConnectorFn[] = [
    injected(
        {
            shimDisconnect: true
        }
    ),
    walletConnect(
        {
            projectId,
            metadata,
            showQrModal: false
        }
    ),
]

const chains = [sepolia, arbitrumSepolia, lineaSepolia] as const

export const config = createConfig({
    chains: chains,
    connectors: connectors,
    transports: {
        [sepolia.id]: http(),
        [arbitrumSepolia.id]: http(),
        [lineaSepolia.id]: http(),
    },
});
