import logoWithText from '/logo-with-text.png';
import { Link, List, Toolbar } from '@mui/material';
import Image from 'components/common/Image';
import { drawerCloseWidth, drawerOpenWidth } from 'components/Main';
import navItems from 'components/sidebar/nav-items';
import NavItem from 'components/sidebar/NavItem';
import { ReactElement } from 'react';
import { rootPaths } from 'routes/paths';
import SimpleBar from 'simplebar-react';

const Sidebar = ({open}: {open: boolean}): ReactElement => {
    return (
        <>
            <Toolbar
                sx={{
                    position: 'fixed',
                    height: 98,
                    zIndex: 1,
                    bgcolor: 'background.default',
                    p: 0,
                    justifyContent: 'center',
                    width: open ? drawerOpenWidth - 1 : drawerCloseWidth - 1,
                }}
            >
                <Link
                    href={rootPaths.homeRoot}
                    sx={{
                        mt: 3,
                    }}
                >
                    <Image
                        src={open ? logoWithText : logoWithText}
                        alt={open ? 'logo with text' : 'logo'}
                        height={open ? 60 : 40}
                    />
                </Link>
            </Toolbar>
            <SimpleBar style={{maxHeight: '100vh'}}>
                <List
                    component="nav"
                    sx={{
                        mt: 24.5,
                        py: 2.5,
                        height: 724,
                        justifyContent: 'top',
                    }}
                >
                    {navItems.map((navItem) => (
                        <NavItem key={navItem.id} navItem={navItem} open={open}/>
                    ))}
                </List>
            </SimpleBar>
        </>
    );
};

export default Sidebar;
