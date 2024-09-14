import App from 'App.tsx';
import React from 'react';
import { useEffect } from 'react';
import { Box, Paper, Typography } from '@mui/material';
import axios from 'axios';

import { useAccount, useAccountEffect } from 'wagmi'

import salesData from 'data/sales-data';
import SaleCard from './SaleCard';


function WalletInfo() {
    const { isConnected, address, chainId } = useAccount()
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

class TodaysSales extends React.Component {
    render() {
        return (
            <Paper sx={{p: {xs: 4, sm: 8}, height: 1}}>
                <Typography variant="h4" color="common.white" mb={1.25}>
                    <WalletInfo />
                </Typography>
                <Typography variant="subtitle2" color="text.disabled" mb={6}>

                </Typography>
                <Box display="grid" gridTemplateColumns="repeat(12, 1fr)" gap={{xs: 4, sm: 6}}>
                    {salesData.map((saleItem) => (
                        <Box key={saleItem.id} gridColumn={{xs: 'span 12', sm: 'span 6', lg: 'span 3'}}>
                            <SaleCard saleItem={saleItem}/>
                        </Box>
                    ))}
                </Box>
            </Paper>
        )
    }
}

export default TodaysSales;
