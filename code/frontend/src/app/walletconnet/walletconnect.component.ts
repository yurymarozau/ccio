import { NgIf } from '@angular/common';
import { Component, CUSTOM_ELEMENTS_SCHEMA, OnInit } from '@angular/core';
import { getAccount, type GetAccountReturnType, watchAccount, type WatchAccountReturnType } from '@wagmi/core'
import { createWeb3Modal } from '@web3modal/wagmi/react'
import { environment } from 'environments/environment';
import { arbitrumSepolia, lineaSepolia, sepolia } from 'viem/chains';
import { createConfig, CreateConnectorFn, http } from 'wagmi';
import { injected, walletConnect } from 'wagmi/connectors';

const projectId = environment.walletConnectProjectId;
const metadata = {
    name: 'CCIO',
    description: 'Crypto Chart IO - CCIO',
    url: 'ccio',
    icons: ['https://avatars.githubusercontent.com/u/37784886'],
};

const connectors: CreateConnectorFn[] = [
    injected(
        {
            shimDisconnect: true
        }
    ),
    walletConnect(
        {
            projectId,
            metadata,
            showQrModal: false
        }
    ),
]

const chains = [sepolia, arbitrumSepolia, lineaSepolia] as const

const wagmiConfig = createConfig({
    chains: chains,
    connectors: connectors,
    transports: {
        [sepolia.id]: http(),
        [arbitrumSepolia.id]: http(),
        [lineaSepolia.id]: http(),
    },
});

@Component({
    selector: 'walletconnect',
    standalone: true,
    imports: [
        NgIf
    ],
    templateUrl: './walletconnect.component.html',
    styleUrl: './walletconnect.component.css',
    schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WalletConnectComponent implements OnInit {
    public modal: any;
    public account: GetAccountReturnType;
    public unwatch: WatchAccountReturnType;

    public ngOnInit(): void {
        this.modal = createWeb3Modal({
            wagmiConfig,
            projectId,
            enableSwaps: false,
            enableOnramp: false,
            allWallets: 'ONLY_MOBILE',
            themeMode: 'light',
        });
        this.account = getAccount(wagmiConfig);
        this.unwatch = watchAccount(wagmiConfig, {
            onChange: this.onChange.bind(this)
        });
    }

    public onChange(account: GetAccountReturnType): void {
        this.account = account;
    }
}
