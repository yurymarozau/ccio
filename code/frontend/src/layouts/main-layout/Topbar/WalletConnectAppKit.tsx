import { Stack } from '@mui/material';

import { createWeb3Modal } from '@web3modal/wagmi/react'

import { config as wagmiConfig } from 'helpers/wagmi/config';
import React from 'react';

const projectId = import.meta.env.FE_WALLETCONNECT_PROJECT_ID;

createWeb3Modal(
    {
        wagmiConfig,
        projectId,
        enableSwaps: false,
        enableOnramp: false,
        allWallets: 'ONLY_MOBILE',
    }
);


class WalletConnectAppKit extends React.Component {
    render () {
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
