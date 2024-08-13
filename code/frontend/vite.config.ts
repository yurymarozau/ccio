import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
import tsconfigPaths from 'vite-tsconfig-paths';


// https://vitejs.dev/config/
export default defineConfig({
    optimizeDeps: {
        include: ['@emotion/react', '@emotion/styled', '@mui/material/Tooltip'],
    },
    plugins: [tsconfigPaths(), react()],
    server: {
        host: '0.0.0.0',
    },
    base: '/',
});
