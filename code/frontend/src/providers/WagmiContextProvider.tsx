import { WagmiAdapter } from '@reown/appkit-adapter-wagmi'
import { baseSepolia, sepolia } from '@reown/appkit/networks'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { WagmiProvider } from 'wagmi';

const queryClient = new QueryClient();
const projectId = import.meta.env.FE_WALLETCONNECT_PROJECT_ID;

export const metadata = {
    name: 'CCIO',
    description: 'CCIO - Crypto Chart IO',
    url: 'ccio',
    icons: [],
};

export const networks = [baseSepolia, sepolia]

export const wagmiAdapter = new WagmiAdapter({
    networks: networks,
    projectId: projectId,
    // transports: {
    //     [sepolia.id]: http(),
    // },
    // connectors: [
    //     injected({
    //         shimDisconnect: false
    //     }),
    //     walletConnect({
    //         projectId,
    //         metadata,
    //         showQrModal: true
    //     }),
    // ],
});


export function WagmiContextProvider({children}) {
    return (
        <WagmiProvider
            config={wagmiAdapter.wagmiConfig}
            reconnectOnMount={true}
        >
            <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
        </WagmiProvider>
    )
}
