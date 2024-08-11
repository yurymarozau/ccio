import {createWeb3Modal} from "@web3modal/wagmi/react";

import {http, createConfig, WagmiProvider} from "wagmi";
import { mainnet, arbitrum, linea } from "viem/chains";
import {walletConnect, coinbaseWallet, injected} from "wagmi/connectors";
import type {CreateConnectorFn} from '@wagmi/core'

import {QueryClient, QueryClientProvider} from "@tanstack/react-query";
import {authConnector,} from "@web3modal/wagmi";

const queryClient = new QueryClient();

const projectId = import.meta.env.WALLETCONNECT_PROJECT_ID;
if (!projectId) throw new Error("Project ID is undefined");

// 2. Create wagmiConfig
const metadata = {
    name: "Web3Modal",
    description: "Web3Modal Example",
    url: "https://web3modal.com",
    icons: ["https://avatars.githubusercontent.com/u/37784886"],
};

// Define chains
const chains = [mainnet, arbitrum, linea] as const

// create the connectors
const connectors: CreateConnectorFn[] = []
connectors.push(walletConnect({projectId, metadata, showQrModal: false}));
connectors.push(injected({shimDisconnect: true}));
connectors.push(coinbaseWallet({
    appName: metadata.name,
    appLogoUrl: metadata.icons[0],
}));

connectors.push(authConnector({
    options: {projectId},
    socials: ['google', 'x', 'github', 'discord', 'apple'], // this will create a non-custodial wallet (please check https://secure.walletconnect.com/dashboard for more info)
    showWallets: true,
    email: true,
    walletFeatures: false,
}));

const wagmiConfig = createConfig({
    chains, // Use the defined chains here
    transports: {
        [mainnet.id]: http(),
        [arbitrum.id]: http(),
        [linea.id]: http(),
    },
    connectors: connectors,
});

// 3. Create modal
createWeb3Modal({wagmiConfig, projectId});

export function AppKitProvider({children}) {
    return (
        <WagmiProvider config={wagmiConfig}>
            <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
        </WagmiProvider>
    )
}

function AppKit() {
    return (
        <div>
            <w3m-button/>
            <p/>
            <w3m-network-button/>
        </div>
    )
}

export default AppKit
