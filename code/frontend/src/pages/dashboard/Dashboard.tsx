import { Box } from '@mui/material';

import WalletInfo from 'components/sections/dashboard/wallet-info/WalletInfo';
import React from 'react';

class Dashboard extends React.Component {
    render() {
        return (
            <>
                <Box display="grid" gridTemplateColumns="repeat(12, 1fr)" gap={3.5}>
                    <Box gridColumn={{xs: 'span 12', '2xl': 'span 8'}} order={{xs: 0}}>
                        <WalletInfo/>
                    </Box>
                </Box>
            </>
        );
    }
}

export default Dashboard;
