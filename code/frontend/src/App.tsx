import React from 'react';
import { AppKitProvider } from 'helpers/wagmi/config.tsx';
import { Outlet } from 'react-router-dom';

class App extends React.Component {
    render() {
        return (
            <AppKitProvider>
                <Outlet/>
            </AppKitProvider>
        )
    }
}

export default App;
