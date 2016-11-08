#!/bin/bash

curl -X POST -H 'Content-Type:application/json' --data-binary '{
    "add-field": {"name":"author",            "type": "string", "docValues": true, "indexed": true, "stored": true},
    "add-field": {"name":"created_at",        "type": "tdate", "docValues": true, "indexed": true, "stored": true},
    "add-field": {"name":"description",       "type": "string", "docValues": true, "indexed": true, "stored": true},
    "add-field": {"name":"html_code",         "type": "tlong", "docValues": true, "indexed": true, "stored": true},
    "add-field": {"name":"html_content",      "type": "text_general", "docValues": false, "indexed": true, "stored": false},
    "add-field": {"name":"html_content_size", "type": "tlong", "docValues": true, "indexed": true, "stored": true},
    "add-field": {"name":"html_fetch_date",   "type": "string", "docValues": true, "indexed": true, "stored": true},
    "add-field": {"name":"link_url",          "type": "string", "docValues": true, "indexed": true, "stored": true},
    "add-field": {"name":"link_url_slug",     "type": "string", "docValues": true, "indexed": true, "stored": true},
    "add-field": {"name":"private",           "type": "tlong", "docValues": true, "indexed": true, "stored": true},
    "add-field": {"name":"saved_by_others",   "type": "tlong", "docValues": true, "indexed": true, "stored": true},
    "add-field": {"name":"tags",              "type": "strings", "docValues": true, "indexed": true, "stored": true},
    "add-field": {"name":"title",             "type": "string", "docValues": true, "indexed": true, "stored": true},
    "add-field": {"name":"to_read",           "type": "tlong", "docValues": true, "indexed": true, "stored": true}
}' http://localhost:8983/solr/pinboard/schema

