const config = [
    {
        context: [
            '/api'
        ],
        target: '',
        secure: true,
        logLevel: 'debug',
        changeOrigin: true,
    },
    {
        context: [
            '/static'
        ],
        target: '',
        secure: true,
        logLevel: 'debug',
        changeOrigin: true,
    }
]

module.exports = config;
