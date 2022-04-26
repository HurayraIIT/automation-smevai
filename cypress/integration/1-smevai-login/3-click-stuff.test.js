/// <reference types="cypress" />

/**
 * Click All The Links
 */

const config = require('../../../util/config.json');

describe('Click Stuff', () => {
  beforeEach(() => {
    cy.session('Login', () => {
      cy.login(config.testing_site, config.trading_admin_email, config.password);
    });
  });

  it('Dashboard', () => {
    cy.visit(config.testing_site);
    cy.url().should('include', '/dashboard');
  });

  it('Product Attribute', () => {
    cy.visit(config.testing_site + '/product/attribute');
    cy.url().should('include', '/product/attribute');
  });
  
  it('Product Items', () => {
    cy.visit(config.testing_site + '/product/item');
    cy.url().should('include', '/product/item');
  });
  
  it('Purchase Invoice', () => {
    cy.visit(config.testing_site + '/purchase/invoice');
    cy.url().should('include', '/purchase/invoice');
    
    cy.visit(config.testing_site + '/purchase/invoice/create');
    cy.url().should('include', '/purchase/invoice/create');
  });
  
  it('Purchase Supplier', () => {
    cy.visit(config.testing_site + '/purchase/supplier');
    cy.url().should('include', '/purchase/supplier');
  });
  
  it('Sales Invoice', () => {
    cy.visit(config.testing_site + '/sales/invoice');
    cy.url().should('include', '/sales/invoice');
    
    cy.visit(config.testing_site + '/sales/invoice/create');
    cy.url().should('include', '/sales/invoice/create');
  });
  
  it('Sales Customer', () => {
    cy.visit(config.testing_site + '/sales/customer');
    cy.url().should('include', '/sales/customer');
  });
  
  it('Transaction History', () => {
    cy.visit(config.testing_site + '/transaction/history');
    cy.url().should('include', '/transaction/history');
  });
  
  it('Transaction Income Expense Category', () => {
    cy.visit(config.testing_site + '/transaction/income-expense-category');
    cy.url().should('include', '/transaction/income-expense-category');
  });
  
  it('Transaction Income', () => {
    cy.visit(config.testing_site + '/transaction/income');
    cy.url().should('include', '/transaction/income');
  });
  
  it('Transaction Expense', () => {
    cy.visit(config.testing_site + '/transaction/expense');
    cy.url().should('include', '/transaction/expense');
  });
  
  it('Transaction Investment', () => {
    cy.visit(config.testing_site + '/transaction/investment');
    cy.url().should('include', '/transaction/investment');
  });
  
  it('Transaction Withdraw', () => {
    cy.visit(config.testing_site + '/transaction/withdraw');
    cy.url().should('include', '/transaction/withdraw');
  });
  
  it('Transaction Asset', () => {
    cy.visit(config.testing_site + '/transaction/asset');
    cy.url().should('include', '/transaction/asset');
  });
});