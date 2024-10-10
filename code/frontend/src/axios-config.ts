import axios from 'axios';
// import {  } from '@reown/appkit-siwe';

const instance = axios.create({
    headers: {
        'Content-Type': 'application/json',
    }
});

instance.interceptors.response.use(
    function (response) {
        return response;
    },
    function (error) {
        if (error.response.status === 403) {

        }
    }
);

export default instance as axios;
