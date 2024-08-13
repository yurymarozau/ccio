import {
    Stack
} from '@mui/material';

import { createWeb3Modal } from '@web3modal/wagmi/react'
import { WagmiProvider } from 'wagmi';

import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

import { config as wagmiConfig } from 'helpers/wagmi/config';

const queryClient = new QueryClient();

const projectId = import.meta.env.WALLETCONNECT_PROJECT_ID;
if (!projectId) throw new Error('Project ID is undefined');

createWeb3Modal(
    {
        wagmiConfig,
        projectId,
        enableSwaps: false,
        enableOnramp: false,
        allWallets: 'ONLY_MOBILE',
    }
);

export function AppKitProvider({children}) {
    return (
        <WagmiProvider config={wagmiConfig}>
            <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
        </WagmiProvider>
    )
}

function WalletConnectAppKit() {
    return (
        <Stack
            direction='row'
            gap={3.75}
            alignItems='center'
            justifyContent='flex-end'
            mr={3.75}
            flex='1 1 20%'
        >
            <w3m-network-button/>
            <w3m-button/>
        </Stack>
    )
}

export default WalletConnectAppKit
