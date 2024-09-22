import { WagmiContextProvider } from 'helpers/wagmi/adapter.tsx';
import { Outlet } from 'react-router-dom';

export default function App() {
    return (
        <WagmiContextProvider>
            <Outlet/>
        </WagmiContextProvider>
    )
}
