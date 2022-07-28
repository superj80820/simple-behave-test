Feature: The Pokemon map for search store

Scenario: Verify store name is existing
  Given first store name
  When the search starts
  Then the map gives specific store