import { AppKitProvider } from 'helpers/wagmi/adapter.tsx';
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
