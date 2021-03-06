/**
 * FastAPI
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.FastApi);
  }
}(this, function(expect, FastApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FastApi.TranslationRequest();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('TranslationRequest', function() {
    it('should create an instance of TranslationRequest', function() {
      // uncomment below and update the code to test TranslationRequest
      //var instane = new FastApi.TranslationRequest();
      //expect(instance).to.be.a(FastApi.TranslationRequest);
    });

    it('should have the property sourceText (base name: "source_text")', function() {
      // uncomment below and update the code to test the property sourceText
      //var instane = new FastApi.TranslationRequest();
      //expect(instance).to.be();
    });

    it('should have the property toLanguage (base name: "to_language")', function() {
      // uncomment below and update the code to test the property toLanguage
      //var instane = new FastApi.TranslationRequest();
      //expect(instance).to.be();
    });

    it('should have the property fromLanguage (base name: "from_language")', function() {
      // uncomment below and update the code to test the property fromLanguage
      //var instane = new FastApi.TranslationRequest();
      //expect(instance).to.be();
    });

    it('should have the property preferredEngine (base name: "preferred_engine")', function() {
      // uncomment below and update the code to test the property preferredEngine
      //var instane = new FastApi.TranslationRequest();
      //expect(instance).to.be();
    });

    it('should have the property withAlignment (base name: "with_alignment")', function() {
      // uncomment below and update the code to test the property withAlignment
      //var instane = new FastApi.TranslationRequest();
      //expect(instance).to.be();
    });

    it('should have the property fallback (base name: "fallback")', function() {
      // uncomment below and update the code to test the property fallback
      //var instane = new FastApi.TranslationRequest();
      //expect(instance).to.be();
    });

  });

}));
