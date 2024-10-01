import PageLoader from 'components/common/PageLoader';
import Splash from 'components/common/Splash';
import { lazy, PropsWithChildren, ReactElement, Suspense } from 'react';
import { createBrowserRouter, Outlet, RouteObject, RouterProps } from 'react-router-dom';
import paths from 'routes/paths';

const App = lazy<() => ReactElement>(() => import('App'));

const Main = lazy<({children}: PropsWithChildren) => ReactElement>(
    () => import('components/Main'),
);


const Dashboard = lazy<() => ReactElement>(() => import('components/dashboard/Dashboard'));
const Error404 = lazy<() => ReactElement>(() => import('components/error/Error404'));

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
                    <Main>
                        <Suspense fallback={<PageLoader/>}>
                            <Outlet/>
                        </Suspense>
                    </Main>
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
        element: <Error404/>,
    },
];

const options: {basename: string} = {
    basename: '/',
};

const router: Partial<RouterProps> = createBrowserRouter(routes, options);

export default router;
