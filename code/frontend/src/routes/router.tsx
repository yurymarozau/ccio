import PageLoader from 'components/loading/PageLoader';
import Splash from 'components/loading/Splash';
import { lazy, PropsWithChildren, ReactElement, Suspense } from 'react';
import { createBrowserRouter, Outlet, RouteObject, RouterProps } from 'react-router-dom';
import paths from './paths';

const App = lazy<() => ReactElement>(() => import('App'));

const MainLayout = lazy<({children}: PropsWithChildren) => ReactElement>(
    () => import('layouts/main-layout'),
);


const Dashboard = lazy<() => ReactElement>(() => import('pages/dashboard/Dashboard'));
const ErrorPage = lazy<() => ReactElement>(() => import('pages/error/ErrorPage'));

const routes: RouteObject[] = [
    {
        element: (
            <Suspense fallback={<Splash/>}>
                <App/>
            </Suspense>
        ),
        children: [
            {
                path: paths.home,
                element: (
                    <MainLayout>
                        <Suspense fallback={<PageLoader/>}>
                            <Outlet/>
                        </Suspense>
                    </MainLayout>
                ),
                children: [
                    {
                        index: true,
                        element: <Dashboard/>,
                    },
                ],
            },
        ],
    },
    {
        path: '*',
        element: <ErrorPage/>,
    },
];

const options: { basename: string } = {
    basename: '/',
};

const router: Partial<RouterProps> = createBrowserRouter(routes, options);

export default router;
