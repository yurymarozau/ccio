import Splash from 'components/common/Splash';
import Dashboard from 'components/dashboard/Dashboard';
import Error404 from 'components/error/Error404';
import Main from 'components/Main';
import { Suspense } from 'react';
import { createBrowserRouter, RouteObject, RouterProps } from 'react-router-dom';
import paths from 'routes/paths';

const routes: RouteObject[] = [
    {
        path: paths.home,
        element: (
            <Suspense fallback={<Splash/>}>
                <Main/>
            </Suspense>
        ),
        children: [
            {
                index: true,
                element: <Dashboard/>
            },
        ],
    },
    {
        path: '*',
        element: <Error404/>,
    },
];

const options: {basename: string} = {
    basename: paths.home,
};

const router: Partial<RouterProps> = createBrowserRouter(routes, options);

export default router;
