/// <reference types="vite/client" />

interface ImportMetaEnv {
    readonly FE_WALLETCONNECT_PROJECT_ID: string
    readonly FE_BE_HOST: string
}

interface ImportMeta {
    readonly env: ImportMetaEnv
}
