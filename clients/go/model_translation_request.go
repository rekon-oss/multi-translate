/*
 * multi-translate
 *
 * Multi-Translate is a unified interface on top of various translate APIs providing optimal translations, persistence, fallback.
 *
 * API version: 0.2.0
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package multitranslateclient
// TranslationRequest struct for TranslationRequest
type TranslationRequest struct {
	// The text to be translated
	SourceText string `json:"source_text"`
	// The ISO-639-1 code of the language to translate the text to
	ToLanguage string `json:"to_language"`
	// The ISO-639-1 code of the language to translate the text from - if notspecified then detection will be attempted
	FromLanguage string `json:"from_language,omitempty"`
	// Which translation engine to use. Choices are microsoft, google, amazon, papago, deepl, yandex and best
	PreferredEngine string `json:"preferred_engine,omitempty"`
	// Whether to return word alignment information or not
	WithAlignment bool `json:"with_alignment,omitempty"`
	// Whether to fallback to the best available engine if the preferred engine does not succeed
	Fallback bool `json:"fallback,omitempty"`
}
