/*
 * multi-translate
 *
 * Multi-Translate is a unified interface on top of various translate APIs providing optimal translations, persistence, fallback.
 *
 * API version: 0.2.0
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package multitranslateclient
// TranslationResponse struct for TranslationResponse
type TranslationResponse struct {
	Engine string `json:"engine"`
	EngineVersion string `json:"engine_version"`
	DetectedLanguageConfidence float32 `json:"detected_language_confidence,omitempty"`
	FromLanguage string `json:"from_language"`
	ToLanguage string `json:"to_language"`
	SourceText string `json:"source_text"`
	TranslatedText string `json:"translated_text"`
	Alignment []map[string]map[string]string `json:"alignment,omitempty"`
}
