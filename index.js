/**
 * Bismillahir Rahmanir Rahim
 * This is the entry point for automation.
 */

"use strict";

const {Builder, By, Key, until} = require('selenium-webdriver');
const config = require('./util/config.json');
const LoginPage = require('./Pages/login_page');
const RegisterPage = require('./Pages/register_page');

function run() {
    
    const driver = new Builder().forBrowser('firefox').build();
    let loginPage = new LoginPage(driver);
    loginPage.login();
}

run();