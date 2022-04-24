/// <reference types="cypress" />

/**
 * Login
 */

 const config = require('../../../util/config.json');
 
 describe('Login Page Test', () => {
  beforeEach(() => {
      cy.login(config.live_site, config.trading_admin_email, config.password);
      
  });
  
  it('Test login functionality', () => {
      cy.url().should('include', '/dashboard');
  });
  
  it('Test session', () => {
      cy.url().should('include', '/dashboard');
  });
  
});