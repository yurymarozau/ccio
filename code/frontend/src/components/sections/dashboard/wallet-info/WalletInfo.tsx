import { Button, Paper, Typography } from '@mui/material';
import axios from 'axios';

import { useAccount, useAccountEffect, useSignMessage } from 'wagmi'


async function handleSignMessage({ signMessageAsync }) {
    let response: any = await signMessageAsync({
        message: Date.now().toString(),
    });
    console.log(response);
}

function WalletInfoFunction() {
    const { signMessageAsync } = useSignMessage();
    const { isConnected, address, chainId } = useAccount();
    useAccountEffect({
        onConnect(data) {
            // axios.get('/api/');
        },
        onDisconnect() {
            // axios.get('/api/v1/health-check/');
        },
    });
    return (
        <>
            <div>
                {isConnected ? (
                    <div>
                        <p>Address: {address}</p>
                        <p>Chain ID: {chainId}</p>
                        <br/>
                        <div>
                            <Button onClick={() => handleSignMessage({ signMessageAsync })}>Sign</Button>
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
