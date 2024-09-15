import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import React from 'react';
import { WagmiProvider, http, createConfig } from 'wagmi';
import { sepolia, arbitrumSepolia, lineaSepolia } from 'viem/chains';
import { walletConnect, injected } from 'wagmi/connectors';
import type { CreateConnectorFn } from '@wagmi/core'

const queryClient = new QueryClient();
const projectId = import.meta.env.FE_WALLETCONNECT_PROJECT_ID;

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

export class AppKitProvider extends React.Component {
    render() {
        return (
            <WagmiProvider
                config={config}
                reconnectOnMount={false}
            >
                <QueryClientProvider client={queryClient}>{this.props.children}</QueryClientProvider>
            </WagmiProvider>
        )
    }
}
