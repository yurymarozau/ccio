import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import type { CreateConnectorFn } from '@wagmi/core'
import React from 'react';
import { arbitrumSepolia, lineaSepolia, sepolia } from 'viem/chains';
import { createConfig, http, WagmiProvider } from 'wagmi';
import { injected, walletConnect } from 'wagmi/connectors';

const queryClient = new QueryClient();
const projectId = import.meta.env.FE_WALLETCONNECT_PROJECT_ID;

const metadata = {
    name: 'CCIO',
    description: 'CCIO - Crypto Chart IO',
    url: 'ccio',
    icons: [],
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
                reconnectOnMount={true}
            >
                <QueryClientProvider client={queryClient}>{this.props.children}</QueryClientProvider>
            </WagmiProvider>
        )
    }
}
