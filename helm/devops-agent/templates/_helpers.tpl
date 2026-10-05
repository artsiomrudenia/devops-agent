{{- define "devops-agent.fullname" -}}
{{- default "devops-agent" .Release.Name -}}
{{- end -}}
