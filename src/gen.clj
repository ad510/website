(ns gen (:require clojure.edn
                  [me.raynes.fs :as fs])
        (:use net.cgrand.enlive-html)
        (:gen-class))

(deftemplate base "base.htm" [pg]
  [:title] (content ((pg 1) :title))
  [[:a (attr= :href (str (pg 0) ".htm"))]] (add-class "sel")
  [[:.submenu (but (id= ((pg 1) :submenu)))]] nil
  [:#pgcontent] (html-content (slurp (str "in/" (pg 0) ".htm"))))

(defn -main []
  (fs/delete-dir "out")
  (fs/copy-dir "in" "out")
  (spit "out/emai1.txt" (clojure.string/join (interpose "," (reverse
    (map-indexed (fn [i c] (mod (- (int c) (* i 42) 1) 256)) (slurp "emai1.txt"))))))
  (doseq [pg (clojure.edn/read-string (slurp "pgs.txt"))]
    (spit (str "out/" (pg 0) ".htm") (apply str (base pg)))))
