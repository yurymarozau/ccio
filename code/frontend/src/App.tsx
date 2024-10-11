import { WagmiContextProvider } from 'providers/WagmiContextProvider';
import { Outlet, RouterProvider } from 'react-router-dom';
import router from 'routes/router';

export default function App() {
    return (
        <WagmiContextProvider>
            <RouterProvider router={router}>
                <Outlet/>
            </RouterProvider>
        </WagmiContextProvider>
    )
}
