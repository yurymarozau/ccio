import { Stack, Typography } from '@mui/material';
import { useBreakpoints } from 'providers/BreakpointsProvider';
import { ReactElement } from 'react';

const Footer = ({open}: { open: boolean }): ReactElement => {
    const {down} = useBreakpoints();

    const isMobileScreen = down('sm');

    return (
        <Stack
            component="footer"
            direction="row"
            justifyContent={{xs: 'center', sm: 'flex'}}
            ml={isMobileScreen ? 0 : open ? 60 : 27.5}
            pr={{xs: 3, sm: 5.175}}
            pb={6.25}
            pl={{xs: 3, sm: 5.25}}
        >
            <Typography variant="subtitle1" sx={{textAlign: {xs: 'center', sm: 'right'}}}>
                Copyright © 2024 Crypto Chart IO Company. All rights reserved.
            </Typography>
        </Stack>
    );
};

export default Footer;
