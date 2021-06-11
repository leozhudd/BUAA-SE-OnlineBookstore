import {request} from '../network/request'
import Vue from 'vue'

Vue.config.productionTip = false

export function login(){
    request({
        url: ''
    }).then(res => {

    }).catch(err => {

    })
}