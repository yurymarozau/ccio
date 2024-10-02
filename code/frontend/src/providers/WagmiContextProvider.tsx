import { WagmiAdapter } from '@reown/appkit-adapter-wagmi'
import { arbitrum, baseSepolia, sepolia } from '@reown/appkit/networks'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { WagmiProvider } from 'wagmi';
import { injected, walletConnect } from 'wagmi/connectors';

import { createAppKit } from '@reown/appkit/react';
import { createSIWE } from 'components/topbar/siwe';

const queryClient = new QueryClient();
const projectId = import.meta.env.FE_WALLETCONNECT_PROJECT_ID;

const metadata = {
    name: 'CCIO',
    description: 'CCIO - Crypto Chart IO',
    url: 'ccio',
    icons: [],
};

const networks = [arbitrum, baseSepolia, sepolia];

const wagmiAdapter = new WagmiAdapter({
    networks: networks,
    projectId: projectId,
    connectors: [
        injected({
            shimDisconnect: true
        }),
        walletConnect({
            projectId,
            metadata,
            showQrModal: true
        }),
    ],
});

const siweConfig = createSIWE(networks.map(network => network.id) as [number]);

createAppKit({
    debug: true,
    adapters: [wagmiAdapter],
    projectId: projectId,
    networks: networks,
    metadata: metadata,
    allWallets: 'ONLY_MOBILE',
    features: {
        swaps: false,
        onramp: false,
        email: false,
        socials: false,
    },
    siweConfig: siweConfig,
    enableWalletConnect: false,
    enableInjected: false,
    enableCoinbase: false,
});

export function WagmiContextProvider({children}) {
    return (
        <WagmiProvider
            config={wagmiAdapter.wagmiConfig}
            reconnectOnMount={false}
        >
            <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
        </WagmiProvider>
    )
}
