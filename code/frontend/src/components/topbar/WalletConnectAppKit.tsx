import { Stack } from '@mui/material';

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
