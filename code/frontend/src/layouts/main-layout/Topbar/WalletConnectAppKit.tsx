import { Stack } from '@mui/material';

import { createAppKit } from '@reown/appkit/react';

import { metadata, networks, wagmiAdapter } from 'helpers/wagmi/adapter';
import React from 'react';

const projectId = import.meta.env.FE_WALLETCONNECT_PROJECT_ID;

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
    enableWalletConnect: false,
    enableInjected: false,
    enableCoinbase: false,
});

class WalletConnectAppKit extends React.Component {
    render() {
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
}

export default WalletConnectAppKit
