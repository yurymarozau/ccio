import { Stack } from '@mui/material';

import { createAppKit } from '@reown/appkit/react';
import { createSIWE } from 'components/topbar/siwe';

import { metadata, networks, wagmiAdapter } from 'providers/WagmiContextProvider';

const projectId = import.meta.env.FE_WALLETCONNECT_PROJECT_ID;

const siweConfig = createSIWE(networks.map(network => network.id) as [number]);

createAppKit({
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

export default function WalletConnectAppKit() {
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
