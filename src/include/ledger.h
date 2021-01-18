/*
 * Public header file for ledger library
 */

#ifndef __LEDGER_H
#define __LEDGER_H

#include <stdlib.h>

/* This is used for the time_t type. */
#include <time.h>


/*********************
 *     STRUCTURES    *
 *********************/

/* Local model of the ledger */
struct ledger;

/* User of a ledger with signature
 * verification information */
struct ledger_user;

struct ledger_account;

struct ledger_txn;



/*********************
 *     FUNCTIONS     *
 *********************/


/*************
 * ACCESSORS *
 *************/

time_t ledger_time_founded(const struct ledger *p_ledger);

int ledger_n_accounts(const struct ledger *p_ledger);

int user_is_founder(const struct ledger *p_ledger, const struct ledger_user *p_user);

int ledger_using_account_number(const struct ledger *p_ledger, int number);

const struct ledger_account* account_by_number(const struct ledger *p_ledger, int number);

int account_number(const struct ledger_account *p_account);
int account_gross_credits(const struct ledger_account *p_account);
int account_gross_debits(const struct ledger_account *p_account);
int account_net_credits(const struct ledger_account *p_account);
int account_net_debits(const struct ledger_account *p_account);

time_t txn_time(const struct ledger_txn *p_txn);
int txn_amount(const struct ledger_txn *p_txn);
int txn_payer_number(const struct ledger_txn *p_txn);
int txn_recipient_number(const struct ledger_txn *p_txn);

int txn_is_valid(const struct ledger *p_ledger, const struct ledger_txn *p_txn);


/*************
 * MUTATORS  *
 *************/














#endif
