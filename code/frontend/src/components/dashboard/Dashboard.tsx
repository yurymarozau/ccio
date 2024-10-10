import { Box } from '@mui/material';

import WalletInfo from 'components/dashboard/WalletInfo';

export default function Dashboard() {
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