import { Paper, Typography } from '@mui/material';
import axios from 'axios';
import React from 'react';

import { useAccount, useAccountEffect } from 'wagmi'


function WalletInfoFunction() {
    const {isConnected, address, chainId} = useAccount()
    useAccountEffect({
        onConnect(data) {
            axios.get('/api/');
        },
        onDisconnect() {
            axios.get('/api/v1/health-check/');
        },
    })
    return (
        <div>
            {isConnected ? (
                <div>
                    <p>Address: {address}</p>
                    <p>Chain ID: {chainId}</p>
                </div>
            ) : (
                <p>Not connected</p>
            )}
        </div>
    )
}

class WalletInfo extends React.Component {
    render() {
        return (
            <Paper sx={{p: {xs: 4, sm: 8}, height: 1}}>
                <Typography variant="h4" color="common.white" mb={1.25}>
                    <WalletInfoFunction/>
                </Typography>
            </Paper>
        )
    }
}

export default WalletInfo;
