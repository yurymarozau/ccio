import { CssBaseline, ThemeProvider } from '@mui/material';
import App from 'App.tsx';
import BreakpointsProvider from 'providers/BreakpointsProvider.tsx';
import React from 'react';
import ReactDOM from 'react-dom/client';
import theme from 'theme/theme.ts';
import 'index.css';

ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <ThemeProvider theme={theme}>
            <BreakpointsProvider>
                <CssBaseline/>
                <App/>
            </BreakpointsProvider>
        </ThemeProvider>
    </React.StrictMode>,
);
