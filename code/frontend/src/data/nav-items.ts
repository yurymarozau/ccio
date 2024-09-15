export interface NavItem {
    id: number;
    path: string;
    title: string;
    icon: string;
    active: boolean;
}

const navItems: NavItem[] = [
    {
        id: 1,
        path: '/',
        title: 'Dashboard',
        icon: 'mingcute:home-1-fill',
        active: true,
    },
    {
        id: 2,
        path: '#!',
        title: 'Portfolio',
        icon: 'mingcute:briefcase-line',
        active: false,
    },
    {
        id: 3,
        path: '#!',
        title: 'Settings',
        icon: 'mingcute:settings-3-line',
        active: false,
    },
];

export default navItems;
