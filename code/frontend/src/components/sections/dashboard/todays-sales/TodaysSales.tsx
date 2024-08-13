import { ReactElement } from 'react';
import { Box, Paper, Typography } from '@mui/material';

import { getAccount } from '@wagmi/core'

import { config as wagmiConfig } from 'helpers/wagmi/config';

import salesData from 'data/sales-data';
import SaleCard from './SaleCard';


const TodaysSales = (): ReactElement => {
    const account = getAccount(wagmiConfig);
    return (
        <Paper sx={{p: {xs: 4, sm: 8}, height: 1}}>
            <Typography variant="h4" color="common.white" mb={1.25}>
                {account.address}
            </Typography>
            <Typography variant="subtitle2" color="text.disabled" mb={6}>
                {account.chainId}
            </Typography>
            <Box display="grid" gridTemplateColumns="repeat(12, 1fr)" gap={{xs: 4, sm: 6}}>
                {salesData.map((saleItem) => (
                    <Box key={saleItem.id} gridColumn={{xs: 'span 12', sm: 'span 6', lg: 'span 3'}}>
                        <SaleCard saleItem={saleItem}/>
                    </Box>
                ))}
            </Box>
        </Paper>
    );
};

export default TodaysSales;
