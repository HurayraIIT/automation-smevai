/**
 * This class is responsible for the Registration
 * functionality testing.
 */

"use strict";
const { Builder, By, Key, until } = require('selenium-webdriver');
const config = require('../util/config.json');

class RegisterPage {
    constructor(driver) {
        this.driver = driver;
    }

    async register() {
        await this.driver.get(`${config.site_to_test}/register`);
    }
}

module.exports = RegisterPage;