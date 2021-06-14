import axios from 'axios'

export function request(config){
    const instance = axios.create({
        baseURL: 'http://127.0.0.1:8008',
        timeout: 5000
    })
    //请求拦截
    instance.interceptors.request.use(config => {
        console.log(config);
        //更改config中不符合服务器要求的信息
        //显示加载图标
        //某些请求必须携带特殊信息，如token
        return config
    }, err => {
        console.log(err);
    })
    //响应拦截
    instance.interceptors.response.use(res => {
        console.log(res);
        return res.data
    }, err => {
        console.log(err);
    })

    //create返回一个Promise 在引用处直接使用
    return instance(config)
}