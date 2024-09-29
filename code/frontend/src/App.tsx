import { WagmiContextProvider } from 'providers/WagmiContextProvider';
import { Outlet } from 'react-router-dom';

export default function App() {
    return (
        <WagmiContextProvider>
            <Outlet/>
        </WagmiContextProvider>
    )
}
