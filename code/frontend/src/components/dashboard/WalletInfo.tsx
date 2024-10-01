import { Button, Paper, Typography } from '@mui/material';
import axios from 'axios-config';
import { useAccount } from 'wagmi';


function WalletInfoFunction() {
    const {isConnected, address, chainId} = useAccount();

    return (
        <>
            <div>
                {isConnected ? (
                    <div>
                        <p>Address: {address}</p>
                        <p>Chain ID: {chainId}</p>
                        <br/>
                        <div>
                            <Button onClick={() => axios.get('/api/v1/auth/web3/siwe/session/')}>Get session</Button>
                        </div>
                    </div>
                ) : (
                    <p>Not connected</p>
                )}
            </div>
        </>
    )
}

export default function WalletInfo() {
    return (
        <Paper sx={{p: {xs: 4, sm: 8}, height: 1}}>
            <Typography variant="h4" color="common.white" mb={1.25}>
                <WalletInfoFunction/>
            </Typography>
        </Paper>
    )
}
