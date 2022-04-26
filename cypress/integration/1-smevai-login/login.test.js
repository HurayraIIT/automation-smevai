/// <reference types="cypress" />

/**
 * Login
 */

const config = require('../../../util/config.json');

describe('Login Page Test', () => {
    beforeEach(() => {
        cy.session("Login", () => {
            cy.login(config.testing_site, config.trading_admin_email, config.password);
        });
    });

    it('Test login functionality', () => {
        cy.visit(config.testing_site);
        cy.url().should('include', '/dashboard');
    });

    it('Test session', () => {
        cy.visit(config.testing_site);
        cy.url().should('include', '/dashboard');
    });

});