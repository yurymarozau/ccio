import { AppKitProvider } from 'helpers/wagmi/config.tsx';
import React from 'react';
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
