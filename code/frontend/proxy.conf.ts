const config = [
    {
        context: [
            '/api'
        ],
        target: 'http://api:8000',
        secure: false,
        logLevel: 'debug',
        changeOrigin: true,
    },
    {
        context: [
            '/static'
        ],
        target: 'http://api:8000',
        secure: false,
        logLevel: 'debug',
        changeOrigin: true,
    }
]

module.exports = config;
